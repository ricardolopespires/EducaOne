"use client";

import Image from "next/image";
import { useCallback, useEffect, useState } from "react";
import { GoSearch } from "react-icons/go";
import { FaUserTie } from "react-icons/fa";

export const Navbar = () => {
  const [navBg, setNavBg] = useState(false);

  // Função para alterar o background do navbar ao rolar a página
  const handleScroll = useCallback(() => {
    if (window.scrollY >= 60) setNavBg(true);
    else setNavBg(false);
  }, []);

  useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, [handleScroll]);

  return (
    <nav className={`fixed w-full transition-all duration-200 h-20 z-[1000] ${navBg ? 'bg-white shadow-md' : ''}`}>
      <div className="flex items-center justify-between h-full w-[90%] xl:w-[80%] mx-auto">
        {/* Logo */}
        <div className="flex-shrink-0">
          <Image 
            src={'/images/logo.png'} 
            width={40} 
            height={40} 
            alt="EducaOne"
            className="object-contain"
          />
        </div>

        {/* Links de Navegação */}
      
         <div className="border border-gray-200 w-[70%] h-11 rounded-full flex
         items-center">
         <GoSearch className="ml-5 text-lg"/>

         </div>
       

        {/* Botão de Login */}
        <a 
          href="/Sign-In" 
          className="grid grid-cols-2 items-center justify-between px-6 py-2 text-base font-medium rounded-full text-white bg-gray-900 hover:bg-gray-800 transition-colors duration-300"
        >
          <span className="rigth-0 bg-white rounded-full text-gray-900 flex items-center justify-center h-7 w-7">
            <FaUserTie className="h-4 w-4" />
            </span>
          <span>Login</span>
        </a>
      </div>
    </nav>
  );
};