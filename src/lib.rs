/*
This code defines two functions: encrypt and decrypt.
The encrypt function takes a plaintext string and a shift value, and returns the ciphertext string. The decrypt function takes a ciphertext string and a shift value,
and returns the plaintext string.

*/
mod benchmarks {
    use super::*;
    use criterion::{black_box, Criterion};

pub fn encrypt(text: &str) -> String {
    let shift = 3;
    let mut result = String::new();
    for c in text.chars() {
        if c.is_ascii_alphabetic() {
            let base = if c.is_ascii_lowercase() { b'a' } else { b'A' };
            let offset = (c as u8 - base + shift) % 26;
            result.push((base + offset) as char);
        } else {
            result.push(c);
        }
    }
    result
}

pub fn decrypt(text: &str) -> String {
    encrypt(text)
}

// Benchmarks
#[bench]
fn encrypt_benchmark(c: &mut Criterion) {
    let text = "This is a sample text to be encrypted.";

    c.bench_function("encrypt", |b| {
        b.iter(|| {
            black_box(encrypt(text));
        });
    });
}

fn decrypt_benchmark(c: &mut Criterion) {
    let text = "Guvf vf n fnzcyr grkg gb or rapelcgrq.";

    c.bench_function("decrypt", |b| {
        b.iter(|| {
            black_box(decrypt(text));
        });
    }

    criterion_group!(benches, encrypt_benchmark, decrypt_benchmark);
    criterion_main!(benches);
}
}

