from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask import url_for

#Initialise REST API
app = Flask(__name__)
api = Api(app)

#create data base
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class BSV_Model(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tag_number = db.Column(db.Integer, nullable=False)
	overall_bsv = db.Column(db.Integer, nullable=False)
	feed = db.Column(db.String(100), nullable=False)
def __repr__(self):
    return f"BSC_value(tag_number = {tag_number}, overall_bsv = {overall_bsv}, feed = {feed})"


    
bsv_put_args = reqparse.RequestParser()
bsv_put_args.add_argument("tag_number", type=int, help="Tag number is required", required=True)
bsv_put_args.add_argument("overall_bsv", type=int, help="overall_bsv is required", required=True)
bsv_put_args.add_argument("feed", type=str, help="feed is requires", required=True)

bsv_update_args = reqparse.RequestParser()
bsv_update_args.add_argument("tag_number", type=int, help="Tag number is required")
bsv_update_args.add_argument("overall_bsv", type=int, help="overall_bsv")
bsv_update_args.add_argument("feed", type=str, help="feed is requires")

resource_fields = {
	'id': fields.Integer,
	'tag_number': fields.Integer,
	'overall_bsv': fields.Integer,
	'feed': fields.String
}


#Class and overwritten get fun
class BSC_value(Resource):
    @marshal_with(resource_fields)
    def get(self,bsv_id):
       result = BSV_Model.query.filter_by(overall_bsv=bsv_id).all()
       if not result:
           abort(404, message="Could not find BSV with that id")
       return result

    @marshal_with(resource_fields)
    def put(self, bsv_id):
        args = bsv_put_args.parse_args()
        result = BSV_Model.query.filter_by(id = bsv_id).first()
        if result:
            abort(409, message="Tag id taken...")
        bsv_new = BSV_Model(id=bsv_id, tag_number=args['tag_number'], overall_bsv=args['overall_bsv'], feed=args['feed'])
        db.session.add(bsv_new)
        db.session.commit()
        return bsv_new, 201

    @marshal_with(resource_fields)
    def patch(self,bsv_id):
        args = bsv_update_args.parse_args()
        result = BSV_Model.query.filter_by(id= bsv_id).first()
        if not result:
            abort(404, message="Id doesn't exist, cannot update")
        if args['tag_number']:
            result.tag_number = args['tag_number']
        if args['overall_bsv']:
            result.overall_bsv = args['overall_bsv']
        if args['feed']:
            result.feed = args['feed']
        db.session.commit()
        return result

    @marshal_with(resource_fields)
    def delete(self,bsv_id):
        result = BSV_Model.query.filter_by(tag_number = bsv_id).first()
        if not result:
            abort(404, message="Id doesn't exist, cannot update")
        db.session.delete(result)
        db.session.commit()
        
#only when we send get request using /helloworld this works
api.add_resource(BSC_value,"/esd_project/BSV_value/<int:bsv_id>")


#Debug mode used while testing
if __name__ == "__main__":
    app.run( debug=True)
    
    

