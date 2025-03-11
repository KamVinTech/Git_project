public class Car {
    private String model;
    private double price;
    private String color;

    // Constructor
    public Car(String model, double price, String color) {
        this.model = model;
        this.price = price;
        this.color = color;
    }

    // Method to get the car model
    public String getModel() {
        return model;
    }

    // Method to get the car price
    public double getPrice() {
        return price;
    }

    // Method to get the car color
    public String getColor() {
        return color;
    }

    public static void main(String[] args) {
        // Creating car objects
        Car car1 = new Car("Toyota Camry", 24000, "Red");
        Car car2 = new Car("Honda Accord", 26000, "Blue");
        Car car3 = new Car("Tesla Model 3", 35000, "White");

        // Displaying car details
        System.out.println("Car 1: Model = " + car1.getModel() + ", Price = $" + car1.getPrice() + ", Color = " + car1.getColor());
        System.out.println("Car 2: Model = " + car2.getModel() + ", Price = $" + car2.getPrice() + ", Color = " + car2.getColor());
        System.out.println("Car 3: Model = " + car3.getModel() + ", Price = $" + car3.getPrice() + ", Color = " + car3.getColor());
    }
}