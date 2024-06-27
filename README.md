# Simulated Campus Services System

The **Simulated Campus Services System** is a web-based application designed to emulate the functionality of campus services at the University of Miami. 
This system is used to validate the behavior of the UWallet application in a controlled environment, allowing testing of features such as door access and point-of-sale transactions.

## Features

- **Door Access Simulation**: Emulates access control for campus buildings and dorm rooms.
- **Point-of-Sale Transactions**: Simulates transactions using Dining Dollars and meal swipes.
- **User Information Retrieval**: Decodes hexadecimal email addresses to query user information from Firestore.
- **Real-time Updates**: Reflects changes immediately in the UWallet app and database.

## Technologies Used

- **Backend**: Python, Flask
- **Database**: Firestore
- **NFC Integration**: Host Card Emulation (HCE), APDU Commands
- **Frontend**: HTML, CSS, JavaScript

## UWallet

**UWallet** is a mobile application designed to enhance campus services at the University of Miami by replacing traditional ID cards with a digital solution using NFC protocols and Host Card Emulation (HCE).
The app provides convenient access to campus facilities and services, improving security and user experience.

<br>This web-based application directly interfaces with the UWallet mobile Android app, that repo can be found [here](https://github.com/nikeemda/UWalletApp).
