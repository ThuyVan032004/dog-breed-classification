import express, { Application } from "express";
import bodyParser from "body-parser";
import cors from 'cors';
import { router as imageRoutes } from './Routes/Routes.Image';

const app : Application = express()

app.use(bodyParser.json({ limit: '50mb' }));
app.use(bodyParser.urlencoded({ extended: true, limit: '50mb', parameterLimit: 50000 }));

const host = 5000

app.use(express.json())
app.use(cors())

app.use("/api/image", imageRoutes)

app.listen(host, () => {
    console.log(`Server listening to host ${host}`)
})

