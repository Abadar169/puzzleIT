import { Form, message } from "antd";
import React from "react";
import { useDispatch } from "react-redux";
import { Link, useNavigate } from "react-router-dom";
import { registerUser } from "../../../apicalls/users";
import { HideLoading, ShowLoading } from "../../../redux/loaderSlice";

function Register() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const onFinish = async (values) => {
    try {
      dispatch(ShowLoading());
      const response = await registerUser(values);

      dispatch(HideLoading());
      if (response.success) {
        message.success(response.message);
        navigate("/login");
      } else {
        message.error(response.message);
      }
    } catch (error) {
      dispatch(HideLoading());
      message.error(error.message);
    }
  };

  return (
    <div className="flex justify-center items-center h-screen w-screen bgimg">
      <div className="card w-400 p-3  form">
        <div className="flex flex-col">
          <h1 className="text-2xl login">
            PuzzleIt - REGISTER
          </h1>
          <div className="divider"></div>

          <Form layout="vertical" className="mt-2" onFinish={onFinish}>
            <Form.Item name="name" label="Name">
              <input type="text" className="input"/>
            </Form.Item>
            <Form.Item name="email" label="Email">
              <input type="text" className="input" />
            </Form.Item>
            <Form.Item name="password" label="Password">
              <input type="password" className="input" />
            </Form.Item>

            <div className="flex flex-col gap-2">
              <button
                type="submit"
                className="button mt-2 w-100"
              >
                Register
              </button>
              <Link to="/login">Already a member? Login</Link>
            </div>
          </Form>
        </div>
      </div>
    </div>
  );
}

export default Register;