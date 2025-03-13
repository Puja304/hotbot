const express = require('express');
const fs = require('fs');
const path = require('path');
const dotenv = require('dotenv');

// Initialize Express
const app = express();

// Load environment variables
dotenv.config();

const GROQ_API_KEY = process.env.GROQ_API_KEY;
const INITIAL_RESPONSE = process.env.INITIAL_RESPONSE;
const INITIAL_MSG = process.env.INITIAL_MSG;
const CHAT_CONTEXT = process.env.CHAT_CONTEXT;

// Middleware to serve static files
app.use('/static', express.static(path.join(__dirname, 'static')));

// Route to serve the main HTML page
app.get('/', (req, res) => {
    fs.readFile(path.join(__dirname, 'static', 'main.html'), 'utf8', (err, data) => {
        if (err) {
            return res.status(500).send('Error loading main.html');
        }
        res.send(data);
    });
});

// Route to get case details from JSON file
app.get('/case_data', (req, res) => {
    fs.readFile(path.join(__dirname, 'case_data.json'), 'utf8', (err, data) => {
        if (err) {
            return res.status(500).send('Error loading case_data.json');
        }
        res.json(JSON.parse(data));
    });
});

// Endpoint to handle chat input (replace with your actual implementation)
app.post('/chat', (req, res) => {
    // Placeholder for chat logic
    res.send({
        response: 'This is a mock response. Implement your chat logic here.'
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});