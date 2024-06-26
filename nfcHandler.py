#from py122u import nfc
from MyNFC import nfc

# Initialize the NFC reader
reader = nfc.Reader()

chip = nfc.Reader._PN532(reader)

def decimal_to_ascii(decimals):
    # Convert each decimal in the list to its ASCII character and join them into a string
    return ''.join(chr(d) for d in decimals)

def select_application(aid):
    print("Attempting to connect to a device...")

    try:
        # Ensure the reader is connected
        reader.connect()
        print("Connection established with the NFC reader.")

        print("Preparing to send SELECT APDU command to the device...")
        header = [0x00, 0xA4, 0x04, 0x00]  # CLA, INS, P1, P2 for SELECT by name
        lc = [len(aid)]  # Lc field - length of AID
        le = [0x00]  # Le field - maximum expected length of the response, set to 0
        apdu = header + lc + aid + le
        # Send the APDU without specifying the protocol
        
        response, sw1, sw2 = reader.send_apdu_command(apdu)
        

        print("response from device:", response)
        
        if response:
            print("Received response from device:", response)
            words = decimal_to_ascii(response)
            print(words)
            
            #Success
            #if response[-2:] == [0x90, 0x00]:
            if sw1 == 90 and sw2 == 0:
                print("Successfully selected application on the device.")
            else:
                print("Application selection failed or returned an unexpected response.")
        else:
            print("No response received from the device.")

    except Exception as e:
        print(f"An error occurred: {e}")
    return words

# Example AID, replace with your actual AID if different