//const redis = require('redis');
import redis from 'redis';
const promisify = require("util").promisify;
const client = redis.createClient();

const asyncGet = promisify(client.get).bind(client);
const asyncSet = promisify(client.set).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  console.log(await asyncGet(schoolName));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
