import React, { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { searchByImage } from '../services/api';

const ImageSearch = ({ onResults, onLoading }) => {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);

  const onDrop = useCallback((acceptedFiles) => {
    const file = acceptedFiles[0];
    if (file) {
      setImage(file);
      const reader = new FileReader();
      reader.onload = () => setPreview(reader.result);
      reader.readAsDataURL(file);
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'image/*': ['.png', '.jpg', '.jpeg', '.gif', '.webp']
    },
    maxFiles: 1
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!image) return;

    onLoading(true);
    try {
      const results = await searchByImage(image);
      onResults(results);
    } catch (error) {
      console.error('Search error:', error);
      alert('Error performing image search. Please try again.');
    } finally {
      onLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Upload Image
        </label>
        <div
          {...getRootProps()}
          className={`border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition-colors ${
            isDragActive
              ? 'border-blue-500 bg-blue-50'
              : 'border-gray-300 hover:border-gray-400'
          }`}
        >
          <input {...getInputProps()} />
          {preview ? (
            <div className="space-y-2">
              <img
                src={preview}
                alt="Preview"
                className="max-h-48 mx-auto rounded"
              />
              <p className="text-sm text-gray-600">
                {image.name} - Click to change
              </p>
            </div>
          ) : (
            <div>
              <p className="text-gray-600">
                {isDragActive
                  ? 'Drop the image here...'
                  : 'Drag & drop an image here, or click to select'}
              </p>
            </div>
          )}
        </div>
      </div>

      <button
        type="submit"
        disabled={!image}
        className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors font-medium disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        Reverse Image Search
      </button>
    </form>
  );
};

export default ImageSearch;

