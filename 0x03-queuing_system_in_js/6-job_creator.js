import kue from 'kue';
const queue = kue.createQueue();

const jobData = {
    phoneNumber: "4153518780",
    message: "This is message of test"
}

const job = queue.create('push_notification_code', jobData).save((err) => {
    if( !err ) console.log(`Notification job created: ${job.id}`);
})

job.on('complete', function() {
    console.log('Notification job completed');

}).on('failed', function(err, done) {
    console.log('Notification job failed');
})
