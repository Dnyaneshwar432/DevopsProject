# Step 1: Use OpenJDK 21 as base image
FROM openjdk:21-jdk-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy JAR file (adjust name if needed)
COPY target/*.jar app.jar

# Step 4: Expose port (Spring Boot default is 8080)
EXPOSE 8080

# Step 5: Run the jar file
ENTRYPOINT ["java", "-jar", "app.jar"]
