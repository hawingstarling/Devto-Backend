import logo from './logo.svg';
import './App.css';
import { AiFillHeart } from '@react-icons/all-files/ai/AiFillHeart';
import { AiOutlineHeart } from '@react-icons/all-files/ai/AiOutlineHeart';
import { FaRegBookmark } from '@react-icons/all-files/fa/FaRegBookmark';
import { FaBookmark } from '@react-icons/all-files/fa/FaBookmark';
import axios from 'axios'
import { useRef, useState, useEffect } from 'react'

function App() {
    const [data, setData] = useState('');
    const [content, setContent] = useState('')
    const [file, setFile] = useState()
    const [previewURL, setPreviewURL] = useState();
    const filePickerRef = useRef()
    const slug = window.location.href
    const path = window.location.pathname
    const [image, setImage] = useState("");
    const [url, setUrl] = useState("");

    // const upLoad = () => {
    //     const data = new FormData()
    //     data.append('file', image)
    //     data.append('upload_preset', 'oblg2wpj')
    //     data.append('cloud_name', 'dhaddpyed')

    //     fetch('https://api.cloudinary.com/v1_1/dhaddpyed/image/upload', {
    //         method: 'post',
    //         body: data  
    //     })
    //     .then(res => res.json())
    //     .then(data => {
    //         console.log(data.url);
    //         setUrl(data.url)
    //     })
    //     .catch((err) => {
    //         console.log(err);
    //     })
    // }

    useEffect(() => {
        const data = new FormData()
        data.append('file', image)
        data.append('upload_preset', 'oblg2wpj')
        data.append('cloud_name', 'dhaddpyed')
    
        fetch('https://api.cloudinary.com/v1_1/dhaddpyed/image/upload', {
            method: 'post',
            body: data  
        })
        .then(res => res.json())
        .then(data => {
            console.log(data.url);
            setUrl(data.url)
        })
        .catch((err) => {
            console.log(err);
        })
    }, [url]);

    const handleSendPost = async () => {
        try {
            const res = await axios.post('http://localhost:5000/api/v1/articles', {
                'title': data,
                'body_markdown': content,
                'slug': slug,
                'path': path,
                'user': "63ef7b21bfac48fc04433536",
                'cover_image': url
            })
            console.log(res);
        } catch (error) {
            console.log(error);
        }
    }
    return (
        <>
        <div className="App">
            <h1>Create new post</h1>

            <input
                type="file"
                onChange={(e) => setImage(e.target.files[0])}
            />
            <img src={url} />
            {/* <button onClick={() => upLoad()}>Upload</button> */}

            <p>Title</p>
            <input type="text" value = {data} onChange = {(e) => setData(e.target.value)} />
            <p>Content</p>
            <input type="text" value = {content} onChange = {(e) => setContent(e.target.value)} />
            
            <button onClick = {() => handleSendPost()} >Send</button>
        </div>

        </>
    );
}

export default App;
