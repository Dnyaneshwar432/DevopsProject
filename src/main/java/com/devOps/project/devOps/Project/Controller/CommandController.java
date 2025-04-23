package com.devOps.project.devOps.Project.Controller;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

@RestController
public class CommandController {

    @GetMapping("/run-command")
    public String runCommand() {
        StringBuilder output = new StringBuilder();
        try {
            // Command you want to run
            String command = "docker ps -a";

            // Execute the command
            Process process = Runtime.getRuntime().exec(command);

            // Get the output stream of the command
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));

            // Read the output line by line
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }

            // Wait for the process to finish
            process.waitFor();

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
            return "Error executing command";
        }

        // Return the command output
        return output.toString();
    }
}
