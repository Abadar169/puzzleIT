const mongoose = require('mongoose');

mongoose.connect(process.env.MONGO_URL)

const connection = mongoose.connection;

connection.on('connected', () => {
    console.log('MongoDB connection Successful');
})

connection.on('error', () => {
    console.log('MongoDB connection Failed');
})

module.exports = connection;
