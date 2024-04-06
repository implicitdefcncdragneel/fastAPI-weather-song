const express = require('express');
const app = express();
const PORT = 3000;

const mockSongResponse = {
    "results": {
        "albummatches": {
            "album": [
                {"name": "Happy Album 1"},
                {"name": "Happy Album 2"}
            ]
        }
    }
};

const mockGeoLocationResponse = [
    { 
        "lat": 11.1111, 
        "lon": 22.2222 
    }
];

const mockWeatherResponse = {
    "weather": [{ 
        "description": "Clear sky" 
    }]
};

app.get('/mockSongSuccess', (req, res) => {
    res.json(mockSongResponse);
});

app.get('/mockWeatherGeo', (req, res) => {
    res.json(mockGeoLocationResponse);
});

app.get('/mockWeatherDescription', (req, res) => {
    res.json(mockWeatherResponse);
});

app.get('/mock400', (req, res) => {
    return res.status(400).json({ error: 'Bad request' });
});

app.get('/mock401', (req, res) => {
    return res.status(401).json({ error: 'Key Error' });
});

app.get('/mock403', (req, res) => {
    return res.status(403).json({ error: 'Forbidden' });
});

app.get('/mock404', (req, res) => {
    return res.status(404).json({ error: 'Not Found' });
});

app.get('/mock429', (req, res) => {
    return res.status(429).json({ error: 'Limit Exceeded' });
});

app.get('/mock500', (req, res) => {
    return res.status(500).json({ error: 'Internal server error' });
});

app.listen(PORT, () => {
    console.log(`Mock server is running on port ${PORT}`);
});
