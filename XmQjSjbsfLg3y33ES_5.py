
def legalbacklog(cases, max_daily_sessions):
    if max_daily_sessions >= len(cases):
           return max(cases.values())
    else:
        return max(max(cases.values()), sum(cases.values()) // max_daily_sessions) if sum(cases.values()) % max_daily_sessions == 0 \
                       else max(max(cases.values()), sum(cases.values()) // max_daily_sessions + 1)

