# Camp Scheduling Assistant

Python application that provided an input of parameters:
- Activities
- Available time slots for activities

It will create a schedule for the activities taking into account conflicts in terms of instructors and rooms. Thus, no instructor is assigned to multiple activities and no room is needed for multple activities at the same time slot.

The generated schedule is random to provide multple options, based of course on the possible combinations.

The theoretical premise of the conflicts is based on graph theory, where each node is unique activity and edges are conflicts between two different activities. The type of conflict is only specified in-code and not in the node-edge level.