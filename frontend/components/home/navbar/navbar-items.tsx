"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

interface NavbarItemProps {
  label: string;
  href: string;
}

export const NavbarItem = ({
  label,
  href,
}: NavbarItemProps) => {
  const pathname = usePathname();
  const isActive = pathname === href;

  return (
    <Link
      href={href}
      className={`
        text-base font-medium transition-colors duration-300
        ${isActive 
          ? 'text-blue-600' 
          : 'text-gray-700 hover:text-blue-600'
        }
      `}
    >
      {label}
    </Link>
  );
};