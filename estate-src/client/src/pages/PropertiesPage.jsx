import React, {useEffect} from 'react'
import {Row, Col, Container} from 'react-bootstrap'
import {useDispatch, useSelector} from 'react-redux'
import Spinner from "../components/Spinner"
import {getProperties} from '../features/properties/propertySlice'
import { toast } from 'react-toastify'
import Property from '../components/Property'

const PropertiesPage = () => {
    const { properties, isLoading, isError, message } = useSelector(
        (state)=> state.properties);
    
    const dispatch = useDispatch();

    useEffect(()=>{
        if (isError){
            toast.error(message)
        }
        
        dispatch(getProperties());
    }, [dispatch]);
    
    if (isLoading) {
        return <Spinner/>;
    }

  return (
   <>
    <Container>
        <Row>
            <Col className='mg-top text-center'>
                <h1>Our catalog of properties</h1>
                <hr className='hr-text'/>
            </Col>
        </Row>

        {
            <>
                <Row className='mt-3'>
                    {properties.map((property)=>(
                        <Col
                        key={property.id}
                        sm={12}
                        md={6}
                        lg={4}
                        xl={3}
                        >
                            <Property property={property}/>
                        
                        </Col>
                    )
                    )}
                </Row>
            </>
        }


    </Container>
   </>
  )
}

export default PropertiesPage