import type { Metadata } from "next";
import localFont from "next/font/local";
import {Poppins} from 'next/font/google';
import "./globals.css";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

const poppins = Poppins({
  weight:["100" , "200", "300" , "400" , "500" , "600", "700" , "800", "900" ],
  subsets: ["latin"],

})

export const metadata: Metadata = {
  title: 'EducaOne | Cursos online - aprenda o que quiser, quando quiser com plataforma de curso online ',
  description: 'Todas as habilidades de que você precisa em um só lugar ',
}
import { ToastContainer} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      
      <body
        className={`${geistSans.variable} ${poppins.className} ${geistMono.variable} antialiased`}
      >
        <ToastContainer /> 
        {children}
      </body>
    </html>
  );
}
