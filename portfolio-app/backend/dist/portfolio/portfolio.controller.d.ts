import { PortfolioService } from './portfolio.service';
import { Portfolio } from './portfolio.entity';
import { CreatePortfolioDto } from './dto/create-portfolio.dto';
export declare class PortfolioController {
    private readonly portfolioService;
    constructor(portfolioService: PortfolioService);
    findAll(): Promise<Portfolio[]>;
    findOne(id: string): Promise<Portfolio>;
    create(createPortfolioDto: CreatePortfolioDto): Promise<Portfolio>;
    update(id: string, createPortfolioDto: CreatePortfolioDto): Promise<Portfolio>;
    remove(id: string): Promise<void>;
}
