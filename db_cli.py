import os
import sys
import json
from database import *


if __name__ == "__main__":
    match sys.argv[1]:
        # python cli_db.py push {year} {month} {day} {event_string}
        case "push":
            year = int(sys.argv[2])
            month = int(sys.argv[3])
            day = int(sys.argv[4])
            event = json.loads(sys.argv[5])

            db = CalendarDB(os.path.join(ROOT))

            db.year(year).month(month).add_event(day, event)
            
        # python cli_db.py solve_tag_id {tag_id}
        case "solve_tag_id":
            tag_id = sys.argv[2]

            with open(os.path.join(ROOT, "tag.json"), "r", encoding="utf-8") as tag_file:
                tags = json.load(tag_file)
            
            print(tags[tag_id]["name"])
        # python cli_db.py solve_group_id {group_ids_json_array}
        case "solve_group_id":
            group_ids = json.loads(sys.argv[2])

            with open(os.path.join(ROOT, "group.json"), "r", encoding="utf-8") as group_file:
                groups = json.load(group_file)
            
            print([groups[str(i)]["name"] for i in group_ids])