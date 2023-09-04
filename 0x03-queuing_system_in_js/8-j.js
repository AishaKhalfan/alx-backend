function createPushNotificationsJobs(jobs, queue){
  //if (typeof(jobs) !== Array) throw Error('Jobs is not an array')
  if (!(jobs instanceof Array)) throw Error('Jobs is not an array')

  jobs.forEach((index) => {
  //const queue = kue.createQueue();
  //const queueName = 'push_notification_code_3';
  const job = queue.create('push_notification_code_3', index)
   .save((error) => {
    if (!error) console.log(`Notification job created: ${job.id}`);
    })
    job.on('complete', () => {
          console.log(`Notification job ${job.id} completed`);
    });
    job.on('failed', (err) => {
          console.log(`Notification job ${job.id} failed: ${err}`);
    });
    job.on('progress', (prog) => {
          console.log(`Notification job ${job.id} ${prog}% complete`);
    });
 })
}
module.exports = createPushNotificationsJobs;
