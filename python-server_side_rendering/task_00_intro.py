#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid Input : template must be a string,"
              f"we got {type(template).__name__}")
        return

    if not isinstance(attendees, list) or \
            not all(isinstance(attend, dict) for attend in attendees):
        print("Invalid Input: attendees must be a list of dictonnaries, "
              f"we got {type(template).__name__}")
        return

    if not template.strip():
        print("Empty Template: Template is empty, "
              "no output files generated.")
        return

    if not attendees:
        print("Empty List of Object: No data provided, "
              "no output files generated")
        return

    for ind, attendees in enumerate(attendees, start=1):
        msg = template
        try:
            for Keys in ["name", "event_title", "event_date",
                         "event_location"]:
                value = attendees.get(Keys, "N/A")
                msg = msg.replace(f"{{{Keys}}}",
                                  value if value is not None else "N/A")

            out_file = f"output_{ind}.txt"
            if os.path.exists(out_file):
                print(f"The file {out_file} are already exists.")
                continue

            with open(out_file, 'w') as invitation:
                invitation.write(msg)

                print(f"The file {out_file} has genereted")

        except Exception as error:
            print("Misssing Data in object: "
                  "An error occured while, creating the "
                  f"invitation, for {attendees.get('name', 'N/A')}: {error}")