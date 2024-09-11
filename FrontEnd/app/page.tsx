'use client';

import { useState, ChangeEvent } from 'react';
import Image from 'next/image';
import axios from 'axios';
import styles from './page.module.css';
import {imageClassificationRoute} from '../app/Api/Api.ImageClassification';

export default function Home() {
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  

  const handleImageUpload = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setSelectedImage(e.target?.result as string);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleLabelChange = () => {
    const label = document.getElementById('image-label');
    if (label?.innerText == "Upload Image") {
      label.innerText = "";
    }
  }

  const handleSubmit = async (event : React.MouseEvent<HTMLButtonElement>) => {
    event.preventDefault();
    if (selectedImage) {
      try {
        const response = await axios.post(imageClassificationRoute, { image: selectedImage });
        const result = response.data.result;
        if(result == 0) {
            alert("The dog breed is a German Shepherd");
        }

        if(result == 1) {
            alert("The dog breed is a Golden Retriever");
        }
        // You can add further logic here to display the result to the user
      } catch (error) {
        console.error('Error classifying image:', error);
        // Handle error (e.g., show an error message to the user)
      }
    } else {
      console.log('No image selected');
      // You might want to show a message to the user to select an image first
    }
  }

  return (
    <div className={styles.container}>
      <h1>Dog Breed Classification</h1>
      <div className={styles.main}>
        <input
          type="file"
          accept="image/*"
          onChange={handleImageUpload}
          className={styles.file_input}
          id="image-file"
        />
        <label 
        htmlFor="image-file"
        id="image-label"
        className={styles.file_label}
        onClick={handleLabelChange}>Upload Image</label>
        {selectedImage && (
          <div className={styles.image_display}>
            <Image
              src={selectedImage}
              alt="Preview"
              width={400}
              height={400}
            />
          </div>
        )}
        <button
        onClick={handleSubmit}>Submit</button>
      </div>
    </div>
  );
}
