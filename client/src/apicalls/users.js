const { default: axiosInstance } = require(".");

export const registerUser = async (payload) => {
    try {
        const response = await axiosInstance.post('https://puzzle-it-abadar169.vercel.app/api/users/register', payload);
        return response.data;
    } catch (error) {
        return error.response.data;
    }
}

export const loginUser = async (payload) => {
    try {
        const response = await axiosInstance.post('https://puzzle-it-abadar169.vercel.app/api/users/login', payload);
        return response.data;
    } catch (error) {
        return error.response.data;
    }
}

export const getUserInfo = async () => {
    try {
        const response = await axiosInstance.post('https://puzzle-it-abadar169.vercel.app/api/users/get-user-info');
        return response.data;
    } catch (error) {
        return error.response.data;
    }
}

