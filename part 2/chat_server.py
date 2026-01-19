import socket
import threading


HOST = '127.0.0.1' # הגדרות שרת
PORT = 12345
clients = {} # מילון לשמירת הלקוחות המחוברים: {שם_לקוח: אובייקט_סוקט}

def handle_client(client_socket, client_address):
    try:
        # שלב 1: קבלת שם הלקוח מיד עם ההתחברות
        client_name = client_socket.recv(1024).decode('utf-8')
        clients[client_name] = client_socket
        print(f"Connected: {client_name} from {client_address}")

        # שליחת הודעת ברוך הבא והסבר על הפורמט
        welcome_msg = (f"Hello {client_name}! To send a message to Tomer for example, "
                       "use the format: Tomer:<Message>")
        client_socket.send(welcome_msg.encode('utf-8'))

        while True:
            # שלב 2: קבלת הודעה בפורמט: "שם_יעד:הודעה"
            data = client_socket.recv(1024).decode('utf-8')
            if not data: break 
            
            if ":" in data:
                target_name, message = data.split(":", 1)
                
                if target_name in clients:
                    # העברת ההודעה ללקוח המבוקש
                    clients[target_name].send(f"[{client_name}]: {message}".encode('utf-8'))
                else:
                    # שליחת הודעת שגיאה עם ירידת שורה למניעת כפילויות בלקוח
                    client_socket.send(f"\nError: User {target_name} not found.".encode('utf-8'))
            else:
                # טיפול בשגיאת פורמט עם ירידת שורה
                format_error = "\n Error: Invalid format. Please use 'RecipientName:<Message>'."
                client_socket.send(format_error.encode('utf-8'))
                
    except:
        pass
    finally:
        # שלב 3: טיפול בניתוק
        for name, sock in list(clients.items()):
            if sock == client_socket:
                print(f"Disconnected: {name}")
                del clients[name] 
                break
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT)) 
    server.listen(5) # תמיכה ב-5 לקוחות
    print(f"Server is running on {HOST}:{PORT}")
    print("Waiting for clients...")

    while True:
        conn, addr = server.accept()
        # שימוש ב-Threads לטיפול במקביל
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()