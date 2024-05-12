import matplotlib.pyplot as plt

def plot_data(plot_type, x_data, y_data):
    if plot_type == 'bar':
        plt.bar(x_data, y_data, color='blue')
        plt.xlabel('X Data')
        plt.ylabel('Y Data')
        plt.title('Bar Chart')
    elif plot_type == 'line':
        plt.plot(x_data, y_data, marker='o')
        plt.xlabel('X Data')
        plt.ylabel('Y Data')
        plt.title('Line Chart')
    elif plot_type == 'scatter':
        plt.scatter(x_data, y_data, color='red')
        plt.xlabel('X Data')
        plt.ylabel('Y Data')
        plt.title('Scatter Plot')
    else:
        print("Invalid plot type specified.")

    plt.grid(True)
    plt.show()

def main():
    plot_type = input("Enter the type of plot (bar, line, scatter): ")
    x_data = input("Enter X data separated by commas (e.g., 1,2,3,4): ")
    y_data = input("Enter Y data separated by commas (e.g., 10,20,30,40): ")

    try:
        x_data = [float(num) for num in x_data.split(',')]
        y_data = [float(num) for num in y_data.split(',')]
        
        if len(x_data) != len(y_data):
            print("Error: X and Y data lists must have the same length.")
            return

        plot_data(plot_type.lower(), x_data, y_data)

    except ValueError:
        print("Error: Please ensure all inputs are numbers and correctly formatted.")

if __name__ == "__main__":
    main()
