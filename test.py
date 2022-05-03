import requests

BASE = "http://127.0.0.1:5000/"


data = [{"tag_number": 101, "overall_bsv": 3,"feed": "normal" },
        {"tag_number": 102, "overall_bsv": 2,"feed": "more feed required" },
        {"tag_number": 103, "overall_bsv": 5,"feed": "less feed" },
      {"tag_number": 104, "overall_bsv": 1,"feed": "more feed required" },
        {"tag_number": 10, "overall_bsv": 2,"feed": "more feed required" },
        {"tag_number": 1033, "overall_bsv": 3,"feed": "normal" },
        {"tag_number": 133, "overall_bsv": 2,"feed": "more feed required" },
        {"tag_number": 1022, "overall_bsv": 4,"feed": "normal" },
        {"tag_number": 1011, "overall_bsv": 1,"feed": "more feed required" },
        {"tag_number": 1056, "overall_bsv": 1,"feed": "more feed required" },
        {"tag_number": 301, "overall_bsv": 3,"feed": "normal" },
        {"tag_number": 402, "overall_bsv": 2,"feed": "more feed required" },
        {"tag_number": 106, "overall_bsv": 5,"feed": "less feed" },
      {"tag_number": 204, "overall_bsv": 1,"feed": "more feed required" },
        {"tag_number": 210, "overall_bsv": 2,"feed": "more feed required" },
        {"tag_number": 2033, "overall_bsv": 3,"feed": "normal" },
        {"tag_number": 301, "overall_bsv": 2,"feed": "more feed required" },
        {"tag_number": 6022, "overall_bsv": 4,"feed": "normal" },
        {"tag_number": 8011, "overall_bsv": 1,"feed": "more feed required" },
        {"tag_number": 5056, "overall_bsv": 1,"feed": "more feed required" },
        {"tag_number": 5011, "overall_bsv": 1,"feed": "more feed required" },
        {"tag_number": 2056, "overall_bsv": 1,"feed": "more feed required" },
        {"tag_number": 501, "overall_bsv": 3,"feed": "normal" },
        {"tag_number": 502, "overall_bsv": 2,"feed": "more feed required" },
        {"tag_number": 606, "overall_bsv": 5,"feed": "less feed" },
      {"tag_number": 704, "overall_bsv": 1,"feed": "more feed required" },
        {"tag_number": 8810, "overall_bsv": 2,"feed": "more feed required" },
        {"tag_number": 2933, "overall_bsv": 3,"feed": "normal" },
        {"tag_number": 3221, "overall_bsv": 2,"feed": "more feed required" },
        {"tag_number": 122, "overall_bsv": 4,"feed": "normal" },
        {"tag_number": 8211, "overall_bsv": 1,"feed": "more feed required" },
        {"tag_number": 356, "overall_bsv": 1,"feed": "more feed required" },
         {"tag_number": 56, "overall_bsv": 1,"feed": "more feed required" },
        ]


# for i in range(len(data)):
#     response = requests.put(BASE + "esd_project/BSV_value/" + str(i), data[i])
#     print(response.json())


# for i in range(len(data)):
#   response = requests.patch(BASE + "esd_project/BSV_value/" + str(i), data[i])
#   print(response.json())

  
requests.delete(BASE + "esd_project/BSV_value/" + "8011")