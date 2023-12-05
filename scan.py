import cv2
import pyzbar.pyzbar as pyzbar

# Start webcam
cap = cv2.VideoCapture(0)
names = set()


# Function for attendance file
attendance_file = 'attendance.txt'
fob = open(attendance_file, 'a+')

def mark_attendance(student_id):
    if student_id in names:
        print(f'{student_id} is already present.')
    else:
        names.add(student_id)
        fob.write(f'{student_id} is present\n') 
        print(f'{student_id} is present.')

print('Reading code...')

while True:
    _, frame = cap.read()
    decode_objects = pyzbar.decode(frame)

    if decode_objects:
        for obj in decode_objects:
            try:
                decoded_data = obj.data.decode('utf-8')
                mark_attendance(decoded_data)
            except UnicodeDecodeError as e:
                print(f'Error decoding data from QR code: {obj.data}')

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Close the attendance file
fob.close()
cap.release()
cv2.destroyAllWindows()