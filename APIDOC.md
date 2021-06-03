# ros_flask API Documentation
Provides communication between the robotic arm's ROS messages and the UI

## Get the camera image
**Request Format:** /img

**Request Type:**  GET

**Returned Data Format**: Plain Text in the format of a jpg. Can set the src of an HTML img element to this text directly. 

**Description:** Returns the plate image. [not yet implemented: dependent on start message letting you know if camera is in correct position]

**Example Request:** /img

**Example Response:**

```
data:image/jpg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhs ...
```

**Error Handling:**
- TODO

## Update the selected image coordinates
**Request Format:** /coords

**Request Type:**  POST

**Returned Data Format**: Plain text

**Description:** Receives the image coordinates from the UI, then sends them off as a ROS message to the robot. 
For the POST request, coordinates are sent in request body as key value pairs

**Example Request:** /coords

**Example Response:**

```
coordinates updated successfuly
```

**Error Handling:**
- TODO