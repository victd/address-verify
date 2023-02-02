import smtplib

# SMTP address verify
# from HHOF rollcall, DIGITS, BI relaunch SP exclusions
# hbrink and pad

server = smtplib.SMTP('mail')
server.set_debuglevel(True)  # show communication with the server
try:
    dhellmann_result = server.verify('dhellmann')
    notthere_result = server.verify('notthere')
finally:
    server.quit()

print ('dhellmann: ' + dhellmann_result)
print ('notthere : ' + notthere_result)
