import numpy as np
import matplotlib.pyplot as plt
import time

# Function to generate a simulated continuous data stream of floating-point numbers
def generate_continuous_data_stream():
    t = 0
    while True:
        
        signal = 5 * np.sin(np.pi * (t % 24) / 24)  # Simulate pattern of floating-point values
        noise = np.random.normal(0, 0.5)  # Random noise 
        # Occasionally introducing an anomaly
        anomaly = np.random.choice([0, 1], p=[0.95, 0.05]) * np.random.uniform(10, 20)#creating anomalies by giving it it execute only 5%of the time and a random value between 10 and 20 where all are equally likely
        data_point = signal + noise + anomaly  # Resulting floating-point value
        yield data_point #to continuously return the data without stopping the flow
        t += 0.1
        time.sleep(0.1)  # to give a small stop

# Function to detect anomalies using  moving_Average
def ma_anomaly_detection(data_point, ma, threshold=3):
    if ma is None:
        ma = data_point  # Initialize MA with the first data point
    else:
        ma = (ma + data_point)/2  # Update MA
    
    # Check if the data point deviates significantly from the MA (anomaly detection)
    if abs(data_point - ma) > threshold:
        anomaly = True
    else:
        anomaly = False
    
    return ma, anomaly

# Function to visualize the continuous data stream and anomalies in real-time
def visualize_continuous_data():
    # Enable interactive plotting
    fig, ax = plt.subplots()
    
    x_data = []
    y_data = []
    anomalies_x = []
    anomalies_y = []
    
    data_stream = generate_continuous_data_stream()  # Start generating continuous floating-point data
    ma = None  # Initialize Moving Average to None
    count=0
    
    for i, data_point in enumerate(data_stream):
        
        # Ensure the data point is a valid float
        
        # Detect anomalies
        ma, is_anomaly = ma_anomaly_detection(data_point, ma, threshold=3)
        
        # Update data lists
        x_data.append(i)
        y_data.append(data_point)
        if is_anomaly:
            anomalies_x.append(i)
            anomalies_y.append(data_point)
            print(f"Anomaly detected at index {i}: {data_point}")  # Print detected anomaly with floating-point precision
        
        # Clear and update plot
        ax.clear() 
        ax.plot(x_data, y_data, label='Data Stream', color='blue')  # Plot the continuous data stream
        ax.scatter(anomalies_x, anomalies_y, color='red', label='Anomalies')  # Highlight anomalies
        
        ax.legend()
        plt.draw()  # Redraw the plot
        plt.pause(0.1)  # pause to update the plot in real time

if __name__ == "__main__":
    visualize_continuous_data()  # Run the real-time visualization of floating-point data  