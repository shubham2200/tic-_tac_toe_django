import os
from logging import Logger 
def get_drive_details():
        #UserComputer().get_drive_details()
        cmd = 'Powershell "Get-PhysicalDisk"'
        try:
            drive_details = []
            for each_line in os.popen(cmd).readlines():
                try:
                    disk_info = str(each_line)

                    if int(disk_info[0]) >= 0:
                        each_line = each_line.split()

                        drive_details.append({
                            'sequence':each_line[0],
                            'disk_type':str(each_line[-7]),
                            'health_status':str(each_line[-4]),
                            'disk_size':str(each_line[-2]) + str(each_line[-1])

                        })
                except:
                    pass
            
            return drive_details
        except:
            logger.error("Unable to get Drive details")
            pass