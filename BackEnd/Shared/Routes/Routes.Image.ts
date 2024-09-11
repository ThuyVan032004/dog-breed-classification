import { imagePredict } from "../Controllers/Controller.Image/ControllerImage";
import express from 'express';

const router = express.Router();

router.post('/prediction', imagePredict)

export { router }