import { PythonShell } from "python-shell";
import { Response, Request } from "express";
import * as fs from "fs";
import * as path from "path";

export const imagePredict = async (req: Request, res: Response) => {
    const base64Image = req.body.image;
    
    if (!base64Image) {
        return res.status(400).json({ error: 'No image data provided' });
    }

    try {
        // Remove the data URL prefix if present
        const base64Data = base64Image.replace(/^data:image\/\w+;base64,/, "");
        
        // Decode base64 to buffer
        const imageBuffer = Buffer.from(base64Data, 'base64');

        // Generate a unique filename
        const filename = `image_${Date.now()}.png`;
        const filepath = path.join(__dirname, '..', '..', '..', 'Shared', filename);
        
        // Write the buffer to a file
        fs.writeFileSync(filepath, imageBuffer);

        const options : {
            mode: 'text',
            pythonPath : string,
            pythonOptions : string[],
            scriptPath : string,
            args : string[]
        } = {
            mode: 'text',
            pythonPath: 'python',
            pythonOptions: ['-u'], // get print results in real-time
            scriptPath: 'E:/dog_breed_classification/LogisticRegressionModel/DogBreedClassification/',
            args: [filepath] 
        };

        const results = await PythonShell.run('Application.py', options);
        console.log(results[0]);
        res.send(results[0]);
        // Clean up: delete the temporary file
        fs.unlinkSync(filepath);
    } catch (error) {
        console.error('Error processing image:', error);
        res.status(500).json({ error: 'Error processing image', details: error.message });
    } 
}