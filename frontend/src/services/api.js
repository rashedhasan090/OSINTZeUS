import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const searchByName = async (name, options) => {
  const response = await api.post('/search/name', {
    name,
    options,
  });
  return response.data;
};

export const searchByImage = async (imageFile) => {
  const formData = new FormData();
  formData.append('image', imageFile);
  
  const response = await api.post('/search/image', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};

export const searchByPhone = async (phone) => {
  const response = await api.get(`/search/phone/${encodeURIComponent(phone)}`);
  return response.data;
};

export const searchByEmail = async (email) => {
  const response = await api.get(`/search/email/${encodeURIComponent(email)}`);
  return response.data;
};

export const searchWiFi = async (location) => {
  const response = await api.post('/search/wifi', {
    location: location || null,
  });
  return response.data;
};

export const generateReport = async (searchResults) => {
  const response = await api.post('/report/generate', {
    search_results: searchResults,
  });
  return response.data;
};

export const getReport = async (reportId) => {
  const response = await api.get(`/report/${reportId}`);
  return response.data;
};

export default api;

