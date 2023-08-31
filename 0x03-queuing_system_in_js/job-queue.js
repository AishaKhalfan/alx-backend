const kue = require('kue');

// Create a Kue queue
const queue = kue.createQueue();

// Create a job
const job = queue.create('email', {
  to: 'example@example.com',
  subject: 'Hello, Kue!',
  text: 'This is a test email from Kue.'
});

// Save the job to the queue
job.save((error) => {
  if (error) {
    console.error('Error saving job to queue:', error);
  } else {
    console.log('Job saved to queue');
  }
  
  // Close the Kue queue connection
  queue.shutdown(5000, () => {
    console.log('Kue queue connection closed');
  });
});

