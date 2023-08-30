//const redis = require('redis');
import redis from 'redis';
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (reject, resolve) => {
    redis.print('Reply ', resolve);
  });
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (reject, resolve) => {
    console.log(resolve);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
