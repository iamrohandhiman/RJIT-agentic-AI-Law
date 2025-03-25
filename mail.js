import nodemailer from "nodemailer";

// Create a transporter using Gmail (note: use app password)
console.log("Initializing email transporter...");
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: "sachin.apwig@gmail.com", // Use environment variables
        pass: "hfnlyodyvjedzrsk"      // Replace with your app password
    }
});

/**
 * Send an email to a specific recipient
 * @param {string} to - Recipient's email address
 * @param {string} subject - Email subject
 * @param {string} text - Email body text
 * @returns {Promise} - Resolves with email info or rejects with error
 */
export function sendEmail(to, subject, text) {
    console.log(`Preparing to send email to: ${to}`);

    // Email configuration
    const mailOptions = {
        from: 'sachin.apwig@gmail.com', // Replace with your email
        to: to,
        subject: subject,
        text: text
    };

    console.log("Sending email...");
    
    // Send email
    return new Promise((resolve, reject) => {
        transporter.sendMail(mailOptions, (error, info) => {
            if (error) {
                console.error('❌ Error sending email:', error);
                reject(error);
            } else {
                console.log('✅ Email sent successfully:', info.response);
                resolve(info);
            }
        });
    });
}

// Example usage
async function exampleUsage() {
    console.log("Starting email sending process...");
    try {
        await sendEmail(
            'rohandhiman2004@gmail.com', 
            'Test Subject', 
            'This is a test email sent from Node.js'
        );
        console.log("🎉 Email process completed successfully.");
    } catch (error) {
        console.error('❌ Failed to send email:', error);
    }
}

// Run example
exampleUsage();
