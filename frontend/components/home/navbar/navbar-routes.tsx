"use client";

import { usePathname } from "next/navigation";
import { NavbarItem } from "./navbar-items";

const guestRoutes = [
  {
    label: "Home",
    href: "/",
  },
  {
    label: "Sobre",
    href: "#about",
  },
  {
    label: "Serviços",
    href: "#services",
  },
  {
    label: "Depoimentos",
    href: "#testimonials",
  },
  {
    label: "Contato",
    href: "/contact",
  },
];

export const NavbarRoutes = () => {
  const pathname = usePathname();

  return (
    <div className="flex items-center gap-8">
      {guestRoutes.map((route) => (
        <NavbarItem
          key={route.href}      
          label={route.label}
          href={route.href}
        />
      ))}
    </div>
  );
};