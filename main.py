import os
import tempfile

import zeep

WS_URL = "http://localhost:8888/ws/reservation?wsdl"

if __name__ == "__main__":
    client = zeep.Client(wsdl=WS_URL)

    print("Szukanie lotów:")
    print(client.service.searchFlights("New York", "London", "2024-04-21"))

    print("Rezerwacja biletu:")
    ticket_id = client.service.bookTicket("0", "Jan Kowalski")
    print("ID biletu:", ticket_id)

    print("Potwierdzenie zakupu:")
    confirmation = client.service.confirmPurchase(ticket_id)
    print(confirmation)

    print("Sprawdzenie rezerwacji:")
    reservation_details = client.service.checkReservation("0")
    print(reservation_details)

    print("Generowanie biletu w formacie PDF:")
    pdf_content = client.service.generateTicketPDF("0")

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_file:
        temp_file.write(pdf_content)
        temp_file_path = temp_file.name

    os.startfile(temp_file_path)  # Otwiera plik PDF w domyślnej aplikacji
