const express = require("express");

const app = express();

app.use(express.json());

const notifications = [];

app.get("/", (req, res) => {
    res.send("Notification API Running");
});

app.get("/notifications", (req, res) => {

    res.json({
        success: true,
        notifications: notifications
    });
});

app.post("/notifications", (req, res) => {

    const notification = req.body;

    notifications.push(notification);

    res.status(201).json({
        success: true,
        message: "Notification Created",
        data: notification
    });
});

app.listen(3000, () => {
    console.log("Server running on port 3000");
});