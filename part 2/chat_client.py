import socket
import threading
import sys

def receive_messages(sock): # פונקציה שמאזינה להודעות נכנסות מהשרת
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')
            if msg:
                # ניקוי השורה הנוכחית מה-"Me: " הקיים והדפסת ההודעה
                sys.stdout.write("\r" + " " * 30 + "\r") 
                print(msg)
                # החזרת סימן הכתיבה למסך
                sys.stdout.write("Me: ")
                sys.stdout.flush()
        except:
            print("\nConnection to server lost.")
            break

def start_client(): # יצירת לקוח
    name = input("Enter your name: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect(('127.0.0.1', 12345))
        client.send(name.encode('utf-8'))

        # קבלת הודעת ההדרכה מהשרת באופן סינכרוני ראשוני
        initial_msg = client.recv(1024).decode('utf-8')
        if initial_msg:
            print(initial_msg)

        # הפעלת תהליכון לקבלת הודעות עתידיות
        threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

        while True:
           
            sys.stdout.write("Me: ")
            sys.stdout.flush()
           
            msg = sys.stdin.readline().strip()
            if msg:
                client.send(msg.encode('utf-8'))
    except Exception as e:
        print(f"Could not connect to server: {e}")

if __name__ == "__main__":
    start_client()