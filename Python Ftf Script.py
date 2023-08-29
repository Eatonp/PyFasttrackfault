Almost out of storage … If you run out, you can't create or edit files, send or receive email on Gmail, or back up to Google Photos.
My Drive
print ('Hello, This program is for Phone line Faults.')
print ('What is the customers name?')
name = input ()
print ('whats the customers wlr3 number?')
wlr3 = input()
print ('whats the customers alternative phone number?')
altp = input()
#------------------------------------------------------
def dialtone():
    print ('Is there a dial tone when phone is the master socket without a filter ?  yes/no')
    while True:
      answer = input ()
      if answer == 'yes':
        qlt ()
      elif answer == 'no':
        global fault
        fault = print ('NDT')
        print ('Run a phone line test in SI')
        lineTest ()
      elif answer != 'yes' and answer != 'no':
        print ('Please enter either yes or no')
            
#-------------------------------------------------------  
def lineTest():
    print ("what was the fault in SI?")
    global siTest
    siTest = input()
    print ('Is this a Fasttrack fault type?')
    while True:
      answer = input ()
      if answer == 'yes':
        fastTrack ()
      elif answer == 'no':
        print ('This is not a Fasttrack fault')
        pdiags ()
      elif answer != 'yes' and answer != 'no':
      
        print ('Please enter either yes or no')
#-----------------------------------------------------------
  
def qlt():
    print('Ask customer to dial 17070')
    print ('Does this read back the correct number?')
    while True:
      answer = input ()
      if answer == 'yes':
        while True:
          print ('Select option 2 for QLT, is this quiet with no noise(1) or crackles(2)? ')
          answer = input ()
          if answer == '1':
            print ('There is no fault on this Wlr3 line.')
            exit ()
          elif answer == '2':
                        lineTest()
                        
          elif answer != 'yes' and answer != 'no':
            print ('Please enter either 1 or 2')
            
      elif answer == 'no':
        global fault
        fault = print ('Possible Crossed Line')
        lineTest()
        

#-----------------------------------------------------------
def fastTrack():
    print ('Does the customer know of any damage within their curtilage?')
    while True:
      answer = input ()
      if answer == 'yes':
        print ('This is not a fasttrack, raise as damage report.')
        exit()
      elif answer == 'no':
        while True:
          print ('Does the customer accept charges?')
          answer = input ()
          if answer == 'no':
            print ('You cannot raise a Enginer unless charges are accepted.')
            print ('')
            fastTrack ()
          elif answer == 'yes':
            print ('what is the time and date these have been accepted?')
            global char
            char = input()
            break
        
          elif answer != 'yes' and answer != 'no':
            print ('Please enter either yes or no')
      
      elif answer != 'yes' and answer != 'no':
        print ('Please enter either yes or no')
        
      break
        
    print ('Is the line fault affecting the customer broadband service?')
    global bb
    bb = input ()
    print ('What is the customers mobile number for text updates? if not wanted just enter n/a')
    global mob
    mob = input ()
    print ('Does the customer want temporary call diversion?  Please make sure customers are aware of addtion charges')
    global tcd
    tcd = input ()
    print ('What is the number the customer would like the call to be diverted to? if not wanted just enter n/a')
    global tcdn
    tcdn = input ()
    print ('Customer contact times?')
    global ct
    ct = input ()
    print ('What is the Si Portal ref?')
    global siref
    siref = input ()
    print ('What is the ERD?')
    global erd
    erd = input ()
    fTf ()
    

#-----------------------------------------------------------
    
def zTk ():
  print ('Does the customer accept charges?')
  while True:
      answer = input ()
      if answer == 'no':
        print ('You cannot raise a Enginer unless charges are accepted.')
        zTk()
      elif answer == 'yes':
        print ('what is the time and date these have been accepted?')
        global char
        char = input()
        break
      elif answer != 'yes' and answer != 'no':
      
        print ('Please enter either yes or no')
        
  print ('Please enter at least 3 avalability slots for an engineer visit.  e.g. 19/09/2017 - AM ')
  global aval
  aval = input ()      
  print ('Is the line fault affecting the customer broadband service?')
  global bb
  bb = input ()
  print ('Customer contact times?')
  global ct
  ct = input ()
  print ('What is the customers mobile number for text updates? if not wanted just enter n/a')
  global mob
  mob = input ()
  print ('Does the customer want temporary call diversion?  Please make sure customers are aware of addtion charges')
  global tcd
  tcd = input ()
  print ('What is the number the customer would like the call to be diverted to? if not wanted just enter n/a')
  global tcdn
  tcdn = input ()
  zenTalk ()

#-----------------------------------------------------------

def zenTalk ():
  print ("\033[1m"'Please enter the following as the first Private note:'"\033[0;0m")
  print ('')
  print ('Fault Type: WLR3 Zen Talk')
  print ('')
  print ('01. Describe the problem experienced by the end user: NC-'+ name +'-DPA, ***** Insert Fault Type here ***** ')
  print ('')
  print ('02. Details of the customers setup: Phone in main socket in the house')
  print ('')
  print ('03. Is the customer kit in the Master Test Socket? Yes')
  print ('')
  print ('04. Has an alternative handset been tried? Yes')
  print ('')
  print ('05. Business next close time:')
  print ('')
  print ('06. Business next open time:')
  print ('')
  print ('07. Appointment Times:' + aval)
  print ('')
  print ('08. Potential Engineer Charges Agreed & Notified' + ' NC- '+ name + ' ' + char)
  print ('')
  print ("\033[1m"'...and enter the following as a Sticky Note:'"\033[0;0m")
  print ('Is the line fault affecting the customer broadband service?'+ bb)
  print ('Contact Name: NC- '+ name +' -DPA,' )
  print ('Contact Number (Not WLR3 Line Number): '+ altp)
  print ('Contact Times:' + ct)
  print ('WLR3 Tel. No. ' + wlr3)
  print ('Does the customer want to receive SMS updates? (Provide Number)' + mob)
  print ('Does the customer require temporary call diversion ' + tcd)
  print ('Number to divert to:' + tcdn)
  print ('SI Line test result: ')
  print ('SI Portal Fault Ref: ')
  print ('ERD / Appointment time/date: ')
  print ('Actions completed so far: ')
  print ('Outstanding Actions: ')
  print ('Have you advised the customer about the fault tracker, public notes and given the fault reference number?')
  print ('1st BT Engineer Date/Notes: ')
  print ('2nd BT Engineer Date/Notes: ')
  print ('3rd BT Engineer Date/Notes:')
  print ('4th BT Engineer Date/Notes:')
  
  #-----------------------------------------------------------

def fTf ():
  print ("\033[1m"'Please enter the following as the first Private note:'"\033[0;0m")
  print ('')
  print ('Fault Type: WLR3 Fasttrack')
  print ('')
  print ('01. Add notes regarding the call - Including full name and DPA details: NC- '+ name +' -DPA, NDT')
  print ('')
  print ('02. Confirm if any known damage in customers curtilage: No damage')
  print ('')
  print ('03. Confirm named contact is aware and agrees to charges if fault is caused by damage in customer curtilage. Please also advise customer to refuse non appointed engineer. Nc -  ' + name + ' -DPA ' + char)
  print ('')
  print ('04. Is the fault affecting customer broadband service? ' + bb)
  print ('')
  print ('05. SI Line test result: ' + siTest)
  print ('')
  print ("\033[1m"'...and enter the following as a Sticky Note:'"\033[0;0m")
  print ("***This is an FastTrack case ****")
  print ("DO NOT APPOINT ENGINEER WITHOUT FULL DIAGS COMPLETED AND CHARGES BEING AGREED.")
  print ("**** Check all notes for details of what has been done already. ****")
  print ('')
  print ('Contact Name: NC- '+ name +' -DPA,' )
  print ('Contact Number (Not WLR3 Line Number): '+ altp)
  print ('Does the customer want to receive SMS updates? (Provide Number)' + mob)
  print ('Does the customer require temporary call diversion ' + tcd)
  print ('Number to divert to: ' + tcdn)
  print ('Contact Times:' + ct)
  print ('WLR3 Tel. No. ' + wlr3)
  print ('SI Line test result: ' + siTest)
  print ('SI Portal Fault Ref: ' + siref)
  print ('ERD: ' + erd )
  print ('Have you advised the customer about the fault tracker, public notes and given the fault reference number ect?: Yes' )
  print ('1st BT Engineer Date/Notes: ')
  print ('2nd BT Engineer Date/Notes: ')
  print ('3rd BT Engineer Date/Notes:')
  print ('4th BT Engineer Date/Notes:')
  print ('')
  print ('')
  print ("\033[1m"'...and enter the following as a PUBLIC Note & Email in zebra'"\033[0;0m")
  print ("Hello,")
  print ('')
  print ('This fault has been raised with our suppliers.  Please review the following important information about how this fault will progress:')
  print ('')
  print ('- The Zen fault owner will provide updates via the online fault tracker, telephone or SMS.  You should not normally need to do anything to progress this fault unless we request additional testing or information from you.')
  print ('')
  print ('- If you need to contact us you may do so using the submission form on the online fault tracker, by e-mailing support@zen.co.uk or by calling 01706 902001.  Please include your fault reference number when e-mailing or calling.')
  print ('')
  print ('- If you have not already done so, please ensure you complete all requested diagnostics to avoid the risk of charges.  You could be liable for charges if an engineer visit identifies a fault with your telephony equipment, internal wiring or if you fail to give BT access to a pre arranged engineer appointment.  An engineer will only be sent following further discussion with you about the fault.')
  print ('')
  print ('Best regards,')
  print ('Technical Support')
  print ('Zen Internet Ltd.')
  print ('01703 902001')
  print ('')
  print ('')
  print ("\033[1m"'...and enter the following as JUST A PUBLIC Note in zebra'"\033[0;0m")
  print ('')
  print ('Hello,')
  print ('BT are indicating to us that they expect to have the fault on your line resolved by ' + erd)
  print ('')
  print ('What will happen next is that BT will attend to your fault and contact you once they have repaired the line.')
  print ('')
  print ('At this point BT do not require access to your premises. If they subsequently advise us that they do, we will contact you.')
  print ('')
  print ('We will monitor for any update from BT and contact you to confirm the fault status when this happens.')
  print ('')
  print ('')
  print ('Best regards,')
  print ('Technical Support')
  print ('Zen Internet Ltd.')
  print ('01703 902001')
  print ('')
  print ('')
  
  #  -----------------------------------------------------------

def pdiags():
    print ('Is the fault present when connected directly into the test socket?')
    while True:
      answer = input ()
      if answer == 'yes':
        print ('Try an alt phone in test socket.  Is the fault present?')
        while True:
          answer = input ()
          if answer == 'yes':
            print ('This will be a non fasttrack fault.  Follow the next steps to raise.')
            zTk ()
          elif answer == 'no':
            print ('Issue may be a faulty faceplate')
          exit()
      elif answer == 'no':
        print ('Issue may be a faulty faceplate')
        exit()
      elif answer != 'yes' and answer != 'no':
      
        print ('Please enter either yes or no')
    exit()
#-----------------------------------------------------------
  
def exit():
    print ('You have reached the end of this program.  Do you wish to restart or close?')
    while True:
      answer = input ()
      if answer == 'restart':
        print ('Restarting program.....')
        pstn()
      elif answer == 'close':
        print ('Issue may be a faulty faceplate')
      elif answer != 'reset' and answer != 'close':
      
        print ('Please enter either restart or close')
        
#-----------------------------------------------------------      

dialtone ()



    