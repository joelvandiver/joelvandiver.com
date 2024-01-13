use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn hello_world() -> PyResult<String> {
    Ok("Hello, world!".to_string())
}

#[pymodule]
fn rust_python_hello_world(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hello_world, m)?)?;
    Ok(())
}
