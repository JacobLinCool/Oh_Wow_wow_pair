import React, { useState, useContext } from 'react'
import { create_post } from '../services/api'
import { AuthContext } from '../services/auth_context'
import { useNavigate } from 'react-router-dom'
import { 
  Container, 
  Card, 
  CardHeader, 
  CardBody, 
  Form, 
  FormGroup, 
  Label, 
  Input, 
  Button 
} from 'reactstrap';

export default function CreatePost() {
    const navigate = useNavigate()
    const auth_context = useContext(AuthContext)
    const dollId = auth_context.currentDollId
    const [postContent, setPostContent] = useState('')
    const [imgFile, setImgFile] = useState(null)

    const handleSubmit = async () => {
        if (!postContent || !imgFile) {
            alert('Please fill in all fields')
            return
        }

        const formData = new FormData();
        formData.append('doll_id', dollId);
        formData.append('content', postContent);
        formData.append('image', imgFile);

        try {
            const res = await create_post(formData)
            console.log('create post success', res.data)
            alert('create post success')
            navigate('/main_page')
        } catch (err) {
            console.error(err)
            // 顯示後端回傳的錯誤訊息
            let msg = 'create post failed';
            if (err.response && err.response.data) {
                const data = err.response.data;
                if (typeof data === 'string') {
                    msg = data;
                } else if (typeof data === 'object') {
                    if (data.detail) {
                        msg = data.detail;
                    } else if (data.non_field_errors) {
                        msg = data.non_field_errors.join(', ');
                    } else {
                        msg = Object.entries(data)
                            .map(([field, messages]) => `${field}: ${Array.isArray(messages) ? messages.join(', ') : messages}`)
                            .join('\n');
                    }
                }
            }
            alert(msg);
        }
    }

    return (
        <Container className="d-flex align-items-center justify-content-center" style={{ minHeight: '100vh', paddingTop: '50px' }}>
            <Card style={{ width: '400px' }}>
                <CardHeader>
                    <h2 className="text-center mb-0">Create Post</h2>
                </CardHeader>
                <CardBody>
                    <Form>
                        <FormGroup>
                            <Input
                                type="textarea"
                                placeholder="Content"
                                value={postContent}
                                onChange={(e) => setPostContent(e.target.value)}
                                className="mb-3"
                            />
                        </FormGroup>
                        
                        <FormGroup>
                            <Input
                                type="file"
                                accept="image/png, image/jpeg, image/gif"
                                onChange={(e) => setImgFile(e.target.files[0])}
                                className="mb-3"
                            />
                        </FormGroup>
                        
                        <Button 
                            block 
                            onClick={handleSubmit}
                            style={{
                                color: '#000',
                                backgroundColor: '#ffd5fc',
                                border: 'none',
                            }}
                        >
                            Create Post
                        </Button>
                    </Form>
                </CardBody>
            </Card>
        </Container>
    )
}
