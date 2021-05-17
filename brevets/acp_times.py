"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    # if else statements to see which range the control distance falls in
    # within each range, more if else statemnts to determine the max time for controls exceding brevet length
    if control_dist_km == 0:
        time = 0
    elif control_dist_km <= 200:
        time = control_dist_km/34
    elif control_dist_km <= 400:
        if brevet_dist_km == 200:
            time = 200/34
        elif brevet_dist_km == 300:
            time = (200/34) + (100/32)
        else:
            time = (200/34) + ((control_dist_km-200)/32)
    elif control_dist_km <= 600:
        if brevet_dist_km == 400:
            time = (200/34) + (200/32)
        else:
            time = (200/34) + (200/32) + ((control_dist_km-400)/30)
    elif control_dist_km <= 1000:
        if brevet_dist_km == 600:
            time = (200/34) + (200/32) + (200/30)
        else:
            time = (200/34) + (200/32) + (200/30) + ((control_dist_km- 600)/28)
    elif control_dist_km <= 1300:
        if brevet_dist_km == 1000:
            time = (200/34) + (200/32) + (200/30) + (400/28)
        else:
            time = (200/34) + (200/32) + (200/30) + (400/28) + ((control_dist_km-1000)/26)
    # round to minute because there are no seconds in calculator
    min = round(time*60)
    # adjusts start time arrow by the minutes found in if else statements
    return brevet_start_time.shift(minutes=min)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    # if else statements to see which range the control distance falls in
    # within each range, more if else statemnts to determine the max time for controls exceding brevet length
    if control_dist_km == 0:
        time = 1
    elif control_dist_km <= 200:
        time = control_dist_km/15
    elif control_dist_km <= 400:
        if brevet_dist_km == 200:
            time = 13.5
        elif brevet_dist_km == 300:
            time = 20
        else:
            time = control_dist_km/15
    elif control_dist_km <= 600:
        if brevet_dist_km == 400:
            time = 27
        else:
            time = control_dist_km/15
    elif control_dist_km <= 1000:
        if brevet_dist_km == 600:
            time = 40
        else:
            time = (600/15) + ((control_dist_km-600)/11.428)
    elif control_dist_km <= 1300:
        if brevet_dist_km == 1000:
            time = 75
        else:
            time = (600/15) + (400/11.428) + ((control_dist_km-1000)/13.333)
    # round to minute because there are no seconds in calculator
    min = round(time*60)
    # adjusts start time arrow by the minutes found in if else statements
    return brevet_start_time.shift(minutes=min)
