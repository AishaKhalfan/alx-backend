const redis = require('redis');
const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '+254712345678',
  message: 'This is a push notification',
};

const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
})
//job.on('created', () => {
  //console.log('Notification job created: ' + job.id);
//});
job.on('completed', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

