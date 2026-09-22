'''
Given a video size, a unit for the video size, a hard drive capacity, and a unit for the hard drive, return the number of videos the hard drive can store using the following constraints:

The unit for the video size can be bytes ("B"), kilobytes ("KB"), megabytes ("MB"), or gigabytes ("GB").
If not given one of the video units above, return "Invalid video unit".
The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
If not given one of the hard drive units above, return "Invalid drive unit".
Return the number of whole videos the drive can fit.
Use the following conversions:
Unit	Equivalent
1 B	1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB
1 TB	1000 GB
'''


def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    videoUnits = {"B": 1, "KB": 1000, "MB": 1000 ** 2, "GB": 1000 ** 3}
    driveUnits = {"GB": 1000 ** 3, "TB": 1000 ** 4}

    if video_unit not in videoUnits:
        return "Invalid video unit"
    if drive_unit not in driveUnits:
        return "Invalid drive unit"

    videosize = video_size * videoUnits[video_unit]
    drivesize = drive_size * driveUnits[drive_unit]

    return int(drivesize // videosize)



print(number_of_videos(500, "MB", 100, "GB")) #should return 200.
print(number_of_videos(1, "TB", 10, "TB")) #should return "Invalid video unit".
print(number_of_videos(2000, "MB", 100000, "MB")) #should return "Invalid drive unit".
print(number_of_videos(500000, "KB", 2, "TB")) #should return 4000.
print(number_of_videos(1.5, "GB", 2.2, "TB")) #should return 1466