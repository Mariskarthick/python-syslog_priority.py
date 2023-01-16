def calculate_syslog_priority(pri):
    facility = pri >> 3
    severity = pri & 7
    return facility, severity

def get_severity_info(severity):
    if severity == 0:
        return "Emergency", "EMERG", "system is unusable"
    elif severity == 1:
        return "Alert", "ALERT", "action must be taken immediately"
    elif severity == 2:
        return "Critical", "CRIT", "critical conditions"
    elif severity == 3:
        return "Error", "ERR", "error conditions"
    elif severity == 4:
        return "Warning", "WARNING", "warning conditions"
    elif severity == 5:
        return "Notice", "NOTICE", "normal but significant condition"
    elif severity == 6:
        return "Informational", "INFO", "informational messages"
    elif severity == 7:
        return "Debug", "DEBUG", "debug-level messages"
    else:
        return "Invalid", "INVALID", "invalid severity level"

pri = int(input("Enter the PRI value: "))
facility, severity = calculate_syslog_priority(pri)
severity_name, severity_key, severity_condition = get_severity_info(severity)

print("PRI value: {}".format(pri))
print("Facility code: {} (local use 0)".format(facility))
print("Severity level: {} ({})".format(severity_name,severity_condition))
print("Severity keyword: {}".format(severity_key))
