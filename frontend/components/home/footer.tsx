import Image from 'next/image';
import Link from 'next/link';
import { FaEnvelope, FaPhone, FaMapMarkerAlt, FaFacebookF, FaTwitter, FaInstagram, FaLinkedinIn } from 'react-icons/fa';

const Footer = () => {
  const quickLinks = [
    { name: 'Sobre Nós', href: '#' },
    { name: 'Serviços', href: '#' },
    { name: 'Projetos', href: '#' },
    { name: 'Blog', href: '#' },
    { name: 'FAQ', href: '#' },
  ];

  const services = [
    { name: 'Gestão de Condomínios', href: '#' },
    { name: 'Controle de Acesso', href: '#' },
    { name: 'Gestão Financeira', href: '#' },
    { name: 'Manutenção', href: '#' },
    { name: 'Suporte 24/7', href: '#' },
  ];

  return (
    <footer className="bg-gray-900 text-white">
      <div className="container mx-auto px-4 py-16">
        {/* Grid Principal */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
          {/* Coluna 1 - Sobre */}
          <div>
            <div className="mb-6">
              <Image src="/images/logo.png" alt="SmartCity" width={150} height={40} />
            </div>
            <p className="text-gray-400 mb-6">
              Transformando a gestão condominial com tecnologia e inovação para uma experiência mais eficiente e moderna.
            </p>
            <div className="flex space-x-4">
              <a href="#" className="bg-blue-600 p-2 rounded-full hover:bg-blue-700 transition-colors">
                <FaFacebookF className="w-5 h-5" />
              </a>
              <a href="#" className="bg-blue-600 p-2 rounded-full hover:bg-blue-700 transition-colors">
                <FaTwitter className="w-5 h-5" />
              </a>
              <a href="#" className="bg-blue-600 p-2 rounded-full hover:bg-blue-700 transition-colors">
                <FaInstagram className="w-5 h-5" />
              </a>
              <a href="#" className="bg-blue-600 p-2 rounded-full hover:bg-blue-700 transition-colors">
                <FaLinkedinIn className="w-5 h-5" />
              </a>
            </div>
          </div>

          {/* Coluna 2 - Links Rápidos */}
          <div>
            <h3 className="text-xl font-bold mb-6">Links Rápidos</h3>
            <ul className="space-y-3">
              {quickLinks.map((link, index) => (
                <li key={index}>
                  <Link href={link.href} className="text-gray-400 hover:text-white transition-colors">
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Coluna 3 - Serviços */}
          <div>
            <h3 className="text-xl font-bold mb-6">Nossos Serviços</h3>
            <ul className="space-y-3">
              {services.map((service, index) => (
                <li key={index}>
                  <Link href={service.href} className="text-gray-400 hover:text-white transition-colors">
                    {service.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Coluna 4 - Contato */}
          <div>
            <h3 className="text-xl font-bold mb-6">Entre em Contato</h3>
            <div className="space-y-4">
              <div className="flex items-start space-x-3">
                <FaPhone className="text-blue-400 text-lg mt-1" />
                <div>
                  <p className="text-gray-400">(11) 4002-8922</p>
                </div>
              </div>
              <div className="flex items-start space-x-3">
                <FaEnvelope className="text-blue-400 text-lg mt-1" />
                <div>
                  <p className="text-gray-400">contato@smartcity.com.br</p>
                </div>
              </div>
              <div className="flex items-start space-x-3">
                <FaMapMarkerAlt className="text-blue-400 text-lg mt-1" />
                <div>
                  <p className="text-gray-400">Av. Paulista, 1000 - São Paulo, SP</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Linha Divisória */}
        <div className="border-t border-gray-800 mt-12 pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <p className="text-gray-400 text-sm">
              © {new Date().getFullYear()} SmartCity. Todos os direitos reservados.
            </p>
            <div className="flex space-x-6 mt-4 md:mt-0">
              <Link href="#" className="text-gray-400 hover:text-white text-sm">
                Termos de Uso
              </Link>
              <Link href="#" className="text-gray-400 hover:text-white text-sm">
                Política de Privacidade
              </Link>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 